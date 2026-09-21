# File Storage & CDN

Roadmap topic 16 · Stage 4: Scale

**Marks:** 🟢 Must Know · 🟡 Good to Know

**In simple words:** store big files (photos, videos) in object storage, not in the database. Let the app upload directly with a signed URL. Serve files through a CDN so they load fast everywhere.

---

#### 1. Object Storage — 🟢 Must Know

*A giant, cheap, reliable folder in the cloud (Amazon S3, Google Cloud Storage).*

1. Stores files as **objects** with a key (`photos/2025/abc.jpg`).
2. Very durable, scales almost without limit, cheap.
3. **Don't** store files in the database (slow, expensive) or on the server's disk (lost when the server is replaced, not shared between servers).
4. The database stores only **metadata** and the file's key.

```text
files table:  id | owner_id | key (photos/abc.jpg) | size | type | created_at
Storage:      photos/abc.jpg → the actual bytes
```

---

#### 2. Upload Flow with Signed URLs — 🟢 Must Know

*The server hands out a short-lived permission slip. The app uploads directly to storage.*

```text
1. App → Server:   "I want to upload photo.jpg" (name, size, type)
2. Server:         checks permission, creates a record, makes a signed upload URL
3. Server → App:   signed URL (valid ~10 minutes)
4. App → Storage:  uploads the file directly to the signed URL
5. App → Server:   "Upload done" (or storage notifies the server)
6. Server:         marks the file as ready
```

Why:

1. The big file never passes through your servers (saves bandwidth and CPU).
2. The URL is temporary and limited to one file.

---

#### 3. Download Flow and Signed URLs — 🟢 Must Know

*Serve public files through the CDN and private files with a temporary link.*

1. **Public files** (profile pictures): serve through the CDN.
2. **Private files** (documents): the server checks permission, then returns a **signed download URL** that expires.
3. Signed URLs let you control access without proxying the file.

**Mobile view:** image libraries (Coil, Glide, SDWebImage) cache downloads, so stable CDN URLs give the best cache hits on the phone.

---

#### 4. CDN (Content Delivery Network) — 🟢 Must Know

*Copies of your files placed on servers close to users.*

```text
User in India → nearby CDN edge → (hit) file returned fast
                              → (miss) fetch from origin storage, keep a copy
```

1. Lower latency, because the file travels a shorter distance.
2. Less load on your origin servers and storage.
3. Best for static, popular files: images, videos, app assets.
4. **Updating files:** use versioned file names (`logo-v3.png`) or invalidate the CDN cache. Otherwise users get old copies until the TTL ends.

---

#### 5. Multipart, Large and Resumable Uploads — 🟡 Good to Know

*Mobile networks drop. Don't restart a 500 MB upload from zero.*

1. Split the file into **chunks** and upload each one (multipart upload).
2. Keep track of which chunks are done, and **resume** from the last one.
3. Retry failed chunks with backoff.
4. Combine the chunks on the storage side when all are uploaded.

---

#### 6. Thumbnails and Cleanup — 🟡 Good to Know

*Different sizes for different screens, and delete what you no longer need.*

1. Create **multiple sizes** (thumbnail, medium, full) in a background job, so the app loads small images first.
2. Validate file **size and type**. Consider virus scanning.
3. **Clean up** abandoned uploads (files uploaded but never confirmed) and orphaned metadata with a scheduled job.

---

#### 7. Common Interview Questions

1. **A user uploads a profile photo. Walk through the flow.**
   Ask the server for a signed URL, upload directly to storage, confirm to the server, the server stores metadata. Serve through the CDN. Generate thumbnails in the background.
2. **Why not store images in the database?**
   Expensive, slow, and hard to scale. Use object storage and keep the key in the database.
3. **What is a signed URL?**
   A temporary URL with permission to upload or download one specific file.
4. **What is a CDN and when do you use it?**
   Edge servers that cache content near users. For static, popular files.
5. **How do you handle large uploads on a bad network?**
   Chunked, resumable uploads with retries.
6. **How do you show a new version of a file when the CDN has cached the old one?**
   Versioned file names or a cache invalidation.

---

#### 8. Common Mistakes

1. Passing big files through the API server.
2. Storing files in the database or on local disk.
3. Making private files publicly accessible.
4. Signed URLs that never expire.
5. No cleanup of abandoned uploads.
6. Serving full-size images to small screens.

---

#### 9. Related Topics

1. `15` Caching
2. `21` Queues, Events & Background Jobs (thumbnails)
3. `30` Mobile-Specific Topics (resumable uploads, image loading)
4. `32` Practice Designs (file storage, video streaming)

---

#### 10. Interview Must Remember

1. Files go in **object storage**; the database keeps **metadata**.
2. **Signed URLs** let the app upload and download directly.
3. **CDN** = files close to the user.
4. **Chunked, resumable uploads** matter on mobile.
5. Generate **thumbnails in the background**, and clean up orphans.
