
What is Token-Based Authentication?
===================================

# 什么是基于令牌的身份验证？

## Introduction

## 介绍


Token-based authentication is a crucial aspect of software development every developer should be familiar with. This article takes a deep dive into the world of token-based authentication, looking at why it's so important and how it's become a must-have for modern app development.

基于令牌的身份验证是软件开发中的一个关键方面，每个开发人员都应该熟悉。本文深入探讨了基于令牌的身份验证的世界，探讨了它为什么如此重要，以及如何成为现代应用开发的必备之物。

Token-based authentication systems are changing the way we think about security, taking a step up from session-based methods, offering a more flexible, secure, and scalable solution. This concept is especially crucial in today's reality of distributed apps and cloud computing. The fact that token-based authentication is so popular just goes to show how effective it is and how much digital security needs have evolved in app development.

令牌式身份验证系统正在改变我们对安全性的看法，它从基于会话的方法中迈出了一步，提供了一种更灵活、安全和可扩展的解决方案。在当今分布式应用和云计算的现实中，这个概念尤为重要。令牌式身份验证如此受欢迎的事实恰恰表明了它的有效性和数字安全需求在应用开发中的演变。  
![](https://media.graphassets.com/resize=width:501,height:500/6STSYUFWTtO4pEp1r3tC)
## Why Not Password and Sessions?

## 为什么不使用密码和会话？


In the traditional session-based authentication mindset, the server maintains the state of the user's session, typically using a session ID stored in a cookie. While functional for simpler, monolithic applications, this model shows its limitations in the face of modern, distributed applications. These limitations manifest in several ways:

在传统的基于会话的身份验证模式中，服务器通过在 cookie 中存储的会话 ID 来维护用户会话的状态。尽管对于简单的单体应用程序而言是可行的，但在现代分布式应用程序面前，这种模式显示出其局限性。这些限制以多种方式体现：

Scalability: Managing session states across multiple servers or microservices can be time-consuming and inefficient.

可扩展性：在多个服务器或微服务之间管理会话状态可能会耗时且效率低下。

Performance: Constantly verifying session information with each request adds overhead, impacting application performance.

性能：每个请求都不断验证会话信息会增加额外开销，影响应用程序的性能。

Security Risks: Sessions can be vulnerable to various attacks, such as session hijacking and cross-site scripting (XSS).

安全风险：会话可能面临各种攻击，如会话劫持和跨站脚本（XSS）攻击。

Token-based authentication addresses these issues by offering a stateless approach. Each token encapsulates the user's identity and permissions, eliminating the need for the server to maintain the session state. This approach doesn’t just simplify the architecture but also enhances security. Tokens, especially when implemented using standards like JWT (JSON Web Tokens), provide strong security features like signing and optional encryption, improving their security against various exploits.

基于令牌的身份验证解决了这些问题，提供了一种无状态的方法。每个令牌都封装了用户的身份和权限，消除了服务器维护会话状态的需要。这种方法不仅简化了架构，还增强了安全性。特别是在使用JWT（JSON Web Tokens）等标准实施的情况下，令牌提供了签名和可选加密等强大的安全功能，提高了对各种攻击的防护能力。  
![](https://media.graphassets.com/resize=width:2299,height:1570/0D0xi7JwR7ijTbojmEkR)
## Token-based Authentication

## 基于令牌的认证


Token-based authentication is not just a technical concept; it's really a fundamental shift in how users and sessions are managed. Simply put, it's like a 'digital pass' that confirms your identity and permissions in a system without the constant need for username and password verification. This pass, or token, can be presented each time a user makes a request, ensuring security without the overhead of traditional methods.

基于令牌的身份验证不仅仅是一个技术概念；它实际上是用户和会话管理方式的根本转变。简而言之，它就像是一个“数字通行证”，在系统中确认您的身份和权限，而无需不断验证用户名和密码。这个通行证，或者令牌，可以在每次用户发送请求时呈现，确保在没有传统方法的开销下实现安全性。

The rise of standards such as OAuth and JWT (JSON Web Tokens) has been instrumental in shaping the landscape of token-based authentication. OAuth provides a framework for authorization, allowing services to verify identities without directly handling user credentials. Meanwhile, JWT has become the de facto standard for tokens, thanks to its compact, URL-safe format and ability to carry a payload of claims. These claims can include user identity, roles, and any other pertinent information, all in an easily verifiable and secure format. These standards have streamlined the implementation of token-based authentication and enhanced compatibility across different systems and services.

OAuth和JWT（JSON Web Tokens）等标准的崛起对基于令牌的身份验证的发展起到了至关重要的作用。OAuth提供了一个授权框架，使得服务可以验证身份，而无需直接处理用户凭证。与此同时，由于它的紧凑、安全的格式和能够携带声明信息的能力，JWT已成为令牌的事实标准。这些声明可以包括用户身份、角色和其他相关信息，全部以易于验证和安全的格式进行传输。这些标准使得基于令牌的身份验证的实施更加简便，并增强了不同系统和服务之间的兼容性。
## How Does Token-Based Authentication Work?

## 令牌基于身份验证的工作原理是什么？


The mechanics of token-based authentication revolve around token creation, distribution, and validation. Here's an overview of the process:

基于令牌的身份验证机制围绕着令牌的创建、分发和验证展开。下面是该过程的概述：

User Authentication: Initially, users log in using their credentials (Traditionally, a username and password, as well as newer methods such as MFA and passkeys). Upon successful authentication, the server generates a token.

用户认证：起初，用户使用他们的凭证登录（传统上是用户名和密码，以及较新的方法，如MFA和密钥）。成功认证后，服务器生成一个令牌。

Translated: 用户认证：最初，用户使用他们的凭证登录（传统上是用户名和密码，以及较新的方法，如MFA和密钥）。成功认证后，服务器生成一个令牌。

Token Generation: This token contains encoded data (or 'claims') about the user. In the case of JWT, these claims include user ID, roles, and token expiry information, all digitally signed to prevent tampering.

令牌生成：此令牌包含有关用户的编码数据（或“声明”）。在JWT的情况下，这些声明包括用户ID，角色和令牌过期信息，全部经过数字签名以防篡改。

Token Transmission: The token is then sent back to the user's client (e.g., a web browser or mobile app).

令牌传输：然后，将令牌发送回用户的客户端（例如，Web浏览器或移动应用程序）。

Client Storage: The client stores this token, usually in local storage or a cookie.

客户端存储：客户端通常将这个令牌存储在本地存储或cookie中。

Token Usage: With each subsequent request to the server, the token is sent along, usually in the HTTP header.

令牌使用：每次对服务器的请求中，通常会将令牌随同发送，放在HTTP头部。

Server Validation: Upon receiving a request with a token, the server validates the token's integrity and authenticity. If valid, the server processes the request according to the claims within the token.

服务器验证：在收到一个带有令牌的请求后，服务器会验证令牌的完整性和真实性。如果令牌有效，服务器会根据令牌中的声明处理请求。

Token revalidation - The auth server revokes the token at certain time intervals, and the client has to recreate it. This way, tokens are safe from session hijacking and are invalidated often.

Token重新验证 - 授权服务器在一定时间间隔内吊销令牌，客户端必须重新创建。通过这种方式，令牌可以在会话劫持情况下保持安全，并且经常失效。  
![](https://media.graphassets.com/resize=width:1470,height:1586/4eLdpGWTASmcptRNlUyw)

An example in pseudo-code might look like this:

一个伪代码的例子可能是这样的：

```java
// User login
const userToken = authenticateUser('username', 'password');
storeTokenLocally(userToken);

// Making an authenticated request
const storedToken = retrieveToken();
makeRequestWithToken('/api/data', storedToken);

// Server-side token validation
function validateRequest(request) {
    const token = extractToken(request);
    if (verifyToken(token)) {
        return processRequest(token);
    } else {
        return 'Invalid token';
    }
}
```

In this example, authenticateUser generates a token upon successful login, storeTokenLocally stores the token, retrieveToken and makeRequestWithToken manages the sending of the token with requests and validateRequest handles token verification server-side.

在这个例子中，authenticateUser在成功登录后生成一个令牌，storeTokenLocally将令牌存储在本地，retrieveToken和makeRequestWithToken用于管理将令牌与请求一起发送，validateRequest用于处理服务端的令牌验证。

在这个例子中，authenticateUser在成功登录后生成一个令牌，storeTokenLocally存储令牌，retrieveToken和makeRequestWithToken管理带有令牌的请求发送，validateRequest处理服务端的令牌验证。
## Token Types

## 令牌类型 (Lìngpái lèixíng)


Diving deeper into token-based authentication, we encounter various types of tokens, each serving specific roles in the authentication and authorization process.

深入探讨基于令牌的身份验证，我们遇到了各种类型的令牌，每种令牌在身份验证和授权过程中扮演特定的角色。

Access Tokens:  These are the backbone of token-based authentication, used to make authenticated requests to a server. Typically short-lived, they contain information about the user and the scope of access granted. For instance, a JWT access token might grant users read access to an API endpoint.

访问令牌：这些是基于令牌的身份验证的核心，用于向服务器发出经过身份验证的请求。通常是短期的，它们包含有关用户和授权访问范围的信息。例如，JWT访问令牌可以向用户授予对API端点的读取访问权限。

Refresh Tokens: Longer-lived than access tokens, refresh tokens are used to obtain new access tokens. They are stored securely on the server and help maintain user sessions without constant re-authentication.

刷新令牌：刷新令牌比访问令牌更长寿，用于获取新的访问令牌。它们被安全地存储在服务器上，帮助保持用户会话而无需持续重新认证。

ID Tokens: Primarily used in OpenID Connect (an identity layer on top of OAuth 2.0), ID tokens provide information about the user. They are often JWTs and contain claims about the user's identity.

ID令牌：主要用于OpenID Connect（OAuth 2.0的身份层）中，ID令牌提供有关用户的信息。它们通常是JWT，并包含有关用户身份的声明。

API Tokens: Often used for server-to-server communication, these tokens grant access to specific API endpoints. Unlike user-specific tokens, API tokens are usually not tied to a specific user's identity but rather to a service or application.

API令牌：通常用于服务器之间的通信，这些令牌授予访问特定API端点的权限。与特定用户的令牌不同，API令牌通常不与特定用户的身份关联，而是与服务或应用程序关联。

Let's consider an example where a user is authenticated via OAuth 2.0:

让我们考虑一个通过OAuth 2.0进行身份验证的示例：

```java
// After successful authentication
const accessToken = getAccessToken();
const refreshToken = getRefreshToken();

// Accessing a protected resource
makeApiCall('/api/userdata', accessToken);

// Refreshing an expired access token
if (isTokenExpired(accessToken)) {
    accessToken = refreshAccessToken(refreshToken);
}
```

In this snippet, getAccessToken and getRefreshToken obtain the respective tokens, makeApiCall uses the access token to request data, and refreshAccessToken is used to obtain a new access token using the refresh token.

在这个片段中，getAccessToken和getRefreshToken获取相应的令牌，makeApiCall使用访问令牌请求数据，而refreshAccessToken则用于使用刷新令牌获取新的访问令牌。
## Challenges in Using Tokens

## 使用令牌的挑战


While token-based authentication offers numerous advantages, it also comes with its own challenges that developers must navigate.

虽然基于令牌的身份验证提供了许多优势，但它也带来了开发者必须解决的挑战。

Token Management: Securely storing and managing tokens, especially refresh tokens, is crucial. Poorly managed tokens can become a security liability.

令牌管理：安全地存储和管理令牌，尤其是刷新令牌，是至关重要的。管理不善的令牌可能会成为安全隐患。

Token Expiration: Implementing and handling token expiration requires careful thought to balance security and user experience.

令牌过期：实施和处理令牌过期需要仔细思考，以平衡安全性和用户体验。

Scalability and Performance: In high-traffic systems, validating tokens for each request can become a performance bottleneck.

可扩展性和性能：在高流量系统中，对于每个请求进行令牌验证可能成为性能瓶颈。

Cross-Domain/Cross-Origin Issues: When tokens are used across different domains, developers need to handle potential CORS (Cross-Origin Resource Sharing) issues.

跨域问题/跨源问题：当令牌在不同的域中使用时，开发者需要处理潜在的跨域资源共享（CORS）问题。

Addressing these challenges often requires a combination of coding best-practices, employing token rotation and revocation strategies, and implementing efficient token validation mechanisms.

解决这些挑战通常需要结合编码最佳实践，采用令牌轮换和吊销策略，并实施高效的令牌验证机制。
## Tokens in Authorization

## 授权令牌


In authorization (the process of deciding if a user is allowed or denied to perform an operation after logging in), tokens can be used as a source of more information about the user. There are two common standards to store data for authorization in tokens.

在授权（登录后决定用户是否允许执行操作的过程）中，令牌可以用作关于用户的更多信息的来源。有两个常见的标准来存储令牌中的授权数据。

Claims: Tokens can carry claims, which are essentially key-value pairs that represent user attributes and privileges. For example, a token might include claims like role: 'admin' or access_level: 'premium'. These claims enable fine-grained control over what resources a user can access.

声明：令牌可以携带声明，这些声明本质上是表示用户属性和权限的键值对。例如，一个令牌可以包含像role: 'admin'或access_level: 'premium'这样的声明。这些声明使得对用户可以访问的资源有了精细的控制。

Scopes: Tokens often define the scope of access, which is the extent of the resources the token allows the user to access. For instance, a token might include an access scope that can be evaluated in policy to decide permissions for the particular identity.

范围：令牌通常定义了访问范围，即令牌允许用户访问的资源范围。例如，一个令牌可能包括一个访问范围，在策略中可以评估该范围以决定特定身份的权限。

Using scopes and claims only to authorize requests can end up with a mess of code that couples application policy with business logic code, making it hard to maintain and audit. The pattern of using imperative if statement and condition functions in the code instead of using them in the right scopes can end up with endless pull requests for simple authorization changes.

仅仅使用作用域和声明来授权请求可能会导致代码混乱，将应用程序策略与业务逻辑代码耦合在一起，使得维护和审计变得困难。在代码中使用命令式的if语句和条件函数来替代正确使用作用域可能会导致无尽的拉取请求，用于简单的授权更改。

This anti-pattern can be illustrated with an example:

这个反模式可以通过一个例子来说明:

```java
// A classic middleware authorizer function
function authorizeUser(token) {
    const userClaims = decodeToken(token).claims;
    if (userClaims.role === 'admin') {
        return 'Full access granted';
    } else if (userClaims.access_level === 'premium') {
        return 'Premium features accessible';
    } else {
        return 'Basic access';
    }
}
```

In this pseudo-code, decodeToken extracts claims from the token, and authorizeUser uses these claims to determine the level of access the user should have. When the product requirements change, we need to change the application code just for this simple policy decision.

在这个伪代码中，decodeToken从令牌中提取声明，authorizeUser使用这些声明来确定用户应该具有的访问级别。当产品需求发生变化时，我们需要修改应用程序代码，仅仅是为了这个简单的策略决策。

在这段伪代码中，decodeToken函数用于从令牌中提取声明，authorizeUser函数则使用这些声明来确定用户应该拥有的访问级别。当产品需求发生变化时，我们需要修改应用程序代码，仅仅是为了这个简单的策略决策。

The proper way to use scopes and claims is to combine them with a Policy-as-Code based authorization system.

使用范围和声明的适当方法是将它们与基于策略与代码的授权系统结合使用。
## Token-based Authentication and Policy as Code

## 基于令牌的身份验证和策略即代码


Token-based authentication synergizes remarkably with the concept of 'Policy as Code'.

基于令牌的身份验证与“策略即代码”的概念良好地协同工作。

Policy languages and engines, such as Open Policy Agent (OPA) or AWS’ Cedar, empower developers to define security and operational policies in code. When coupled with token-based authentication, these policies result in a powerful, flexible system for controlling access to resources.

策略语言和引擎，例如Open Policy Agent（OPA）或AWS的Cedar，赋予开发人员在代码中定义安全和运营策略的能力。当与基于令牌的身份验证结合时，这些策略将产生一个强大、灵活的系统，用于控制对资源的访问。

Automated Policy Enforcement: By defining policies as code, organizations can automatically enforce security rules, reducing the risk of human error and increasing compliance.

自动化政策执行：通过将政策定义为代码，组织可以自动执行安全规则，降低人为错误的风险并提高合规性。

Dynamic Access Control: When integrated with policy engines, Token-based authentication allows for dynamic and context-aware access decisions. The token’s claims can be evaluated against the coded policies to determine if a request should be allowed.

动态访问控制：当与策略引擎集成时，基于令牌的身份验证可以实现动态和上下文意识的访问决策。可以根据令牌的声明与编码策略进行评估，以确定是否应该允许请求。

Here’s an example of how policy as code might work with token-based authentication:

这是一个示例，说明了策略即代码如何与基于令牌的身份验证一起工作。

```java
const userToken = getUserToken();⁠
const policyDecision = policyEngine.evaluate(userToken, 'accessResource');

if (policyDecision.allowed) {
    grantAccessToResource();
} else {
    denyAccess();
}
```

In this scenario, getUserToken retrieves the user’s token, and policyEngine.evaluate assesses this token against predefined policies to decide on resource access. When product requirements change, the only need is to change the policy itself, while application code and logic stay the same.

在这种情况下，getUserToken获取用户的令牌，而policyEngine.evaluate根据预定义的策略评估此令牌来决定资源访问权限。当产品需求变化时，唯一需要改变的是策略本身，应用程序代码和逻辑保持不变。

Authorization-as-a-service solutions like Permit.io allow you to take this integration of policy engines another step forward. Permit allows you to create intricate authorization policies with a no-code UI (Or API), which generates code for you and pushes any updates or changes to your application in real-time.

授权即服务解决方案，如Permit.io，使您能够将策略引擎的集成推进到另一个更高水平。Permit允许您使用无代码的用户界面（或API）创建复杂的授权策略，它会为您生成代码，并实时将任何更新或更改推送到您的应用程序中。
## Conclusion

## 结论


Embracing token-based authentication in your applications is more than just a security measure; it's a step towards more scalable, flexible, and secure systems. Services like Permit.io can significantly streamline the implementation of sophisticated authentication and authorization mechanisms in your applications.

在您的应用程序中采用基于令牌的身份验证不仅仅是一种安全措施，它也是迈向更可扩展、灵活和安全系统的步骤。像Permit.io这样的服务可以大大简化在您的应用程序中实现复杂身份验证和授权机制的过程。

Want to learn more about the world of IAM? Join our Slack community, where hundreds of devs are building and implementing authentication and authorization.

想要更多了解IAM世界吗？加入我们的Slack社区，数百名开发人员正在构建和实现身份验证和授权。