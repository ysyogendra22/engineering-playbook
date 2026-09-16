# Client & Server Basics --- FAANG Interview Notes

#### 1. Definition --- Must Know

1.  **Client** --- application that sends requests to a server, such as
    an Android, iOS, or web app.
2.  **Server** --- system that receives requests, performs processing,
    and returns responses.
3.  **Backend** --- APIs, business logic, authentication, and data
    access running on the server side.

``` text
Client → Request → Server
Client ← Response ← Server
```

#### 2. Why Client--Server Architecture Is Used --- Must Know

1.  Keeps application UI separate from backend logic and data.
2.  Allows Android, iOS, and web clients to use the same backend.
3.  Centralizes business rules and data access.
4.  Allows clients and backend services to scale independently.

``` text
Android ─┐
iOS ─────┼──→ Backend → Database / Cache
Web ─────┘
```

#### 3. Request--Response Lifecycle --- Must Know

``` text
User Action
    ↓
Client
    ↓
HTTP/HTTPS Request
    ↓
Backend API
    ↓
Business Logic
    ↓
Cache / Database
    ↓
HTTP Response
    ↓
Client
    ↓
Update UI
```

1.  User performs an action.
2.  Client creates an HTTP request.
3.  Server receives and validates the request.
4.  Backend executes business logic.
5.  Backend may read/write cache or database.
6.  Server returns an HTTP response.
7.  Client processes the response and updates the UI.

#### 4. HTTP Request --- Must Know

A request commonly contains:

1.  **Method** --- GET, POST, PUT, PATCH, DELETE.
2.  **Endpoint** --- resource being accessed.
3.  **Headers** --- metadata such as authorization.
4.  **Query Parameters** --- pagination, filtering, sorting, etc.
5.  **Body** --- data sent to the server when required.

Example:

``` http
GET /posts?page=1
Authorization: Bearer <token>
```

Common methods:

``` text
GET     → Read
POST    → Create
PUT     → Replace
PATCH   → Update
DELETE  → Delete
```

#### 5. HTTP Response --- Must Know

A response commonly contains:

1.  **Status Code** --- result of the request.
2.  **Headers** --- response metadata.
3.  **Body** --- returned data, commonly JSON.

Important status codes:

``` text
200 → Success
201 → Created
400 → Bad Request
401 → Authentication required/failed
403 → Authenticated but not allowed
404 → Not Found
429 → Too Many Requests
500 → Server Error
```

#### 6. Example --- Loading a List of Posts --- Must Know

Client sends:

``` http
GET /posts?page=1
```

Backend flow:

``` text
Mobile App
    ↓
GET /posts
    ↓
Backend API
    ↓
Validate / Authenticate
    ↓
Business Logic
    ↓
Cache
    ↓ miss
Database
    ↓
Backend
    ↓
JSON Response
    ↓
Mobile App
```

Example response:

``` json
{
  "posts": [
    {
      "id": 1,
      "title": "System Design Basics"
    },
    {
      "id": 2,
      "title": "Backend Engineering"
    }
  ]
}
```

The client parses the response and displays the posts.

#### 7. Stateless Communication --- Good to Know

1.  HTTP requests are generally treated as **stateless**.
2.  The server should not rely on the previous request being available
    automatically.
3.  Authentication information is commonly sent using a token, cookie,
    or session identifier.

``` text
Request 1 → Server
Request 2 → Server
```

Each request should contain the information required to process it.

#### 8. Network Failures & Latency --- Must Know

A client should expect failures such as:

1.  No network connection.
2.  Timeout.
3.  Server unavailable.
4.  Authentication failure.
5.  Rate limiting.
6.  Server error.

Response time can include:

``` text
Network Latency
+
Server Processing
+
Cache / Database Time
```

#### 9. Client vs Server Responsibilities --- Must Know

**Client**

1.  Display UI.
2.  Collect user input.
3.  Send requests.
4.  Handle responses and errors.
5.  Maintain client-side state.

**Server**

1.  Validate requests.
2.  Authenticate and authorize users.
3.  Execute business logic.
4.  Access databases and caches.
5.  Return responses.

#### 10. Common Interview Questions

1.  Explain client-server architecture.
2.  What happens when a mobile app calls an API?
3.  What is inside an HTTP request and response?
4.  Explain `401` vs `403`.
5.  What happens when the server is slow or unavailable?
6.  Trace loading a list of posts from client to database and back.
7.  Why should a mobile client not connect directly to the database?

#### 11. Common Mistakes

1.  Assuming the client directly accesses the backend database.
2.  Assuming every network request succeeds.
3.  Confusing authentication with authorization.
4.  Confusing `401` and `403`.
5.  Ignoring latency, timeout, and server failures.
6.  Storing backend secrets inside a mobile application.

#### 12. Related Topics

1.  HTTP / HTTPS.
2.  REST APIs.
3.  DNS.
4.  TCP/IP.
5.  Authentication & Authorization.
6.  Database & Cache.
7.  Load Balancer.

#### 13. Interview Must Remember

1.  **Client sends requests; server processes them and returns
    responses.**
2.  Understand the full flow: **Client → API → Backend → Cache/DB →
    Response → Client**.
3.  Know the basic parts of an **HTTP request and response**.
4.  Know common HTTP methods and important status codes.
5.  Network calls have **latency and can fail**.
6.  Understand the basic separation of **client and server
    responsibilities**.
7.  Be able to trace one request end-to-end during an interview.
