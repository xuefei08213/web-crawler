
OAuth vs. JWT: What's the Difference for Application Development
================================================================

# OAuth和JWT之间在应用程序开发中有何区别？

## Introduction

## 介绍


In recent years, two prominent technologies have become widely used in web app security: OAuth and JSON Web Tokens (JWT). While both play a critical role in the authentication and authorization processes, they serve distinct purposes and operate under different principles. This article delves into the specifics of OAuth and JWT, comparing their functionalities, use cases, and how they complement each other in securing web applications.

近年来，在Web应用安全方面，两个显著的技术已经广泛应用：OAuth和JSON Web Tokens（JWT）。虽然两者在身份验证和授权过程中起着关键作用，但它们具有不同的目的和运作原则。本文深入探讨了OAuth和JWT的具体内容，比较了它们的功能、用途，并介绍了它们如何在保护Web应用程序方面相互补充。

翻译结果：
近年来，在Web应用安全方面，两个显著的技术已经广泛应用：OAuth和JSON Web Tokens（JWT）。虽然两者在身份验证和授权过程中起着关键作用，但它们具有不同的目的和运作原则。本文深入探讨了OAuth和JWT的具体内容，比较了它们的功能、用途，并介绍了它们如何在保护Web应用程序方面相互补充。
## JWT: The Self-Contained Token

## JWT: 自包含的令牌


The JWT is a compact, URL-safe token format primarily used to transmit information between parties securely. It's a JSON object that can encode a variety of claims, such as user identity and attributes. The beauty of JWTs lies in their self-contained nature, meaning the token itself holds all necessary information, which is verified through digital signatures.

JWT（JSON Web Token）是一种紧凑、URL安全的令牌格式，主要用于安全地在各方之间传输信息。它是一个JSON对象，可以编码各种声明，如用户身份和属性。JWT的优点在于它的自包含性，也就是说令牌本身包含了所有必要的信息，并通过数字签名进行验证。

To understand JWTs, let's explore their structure, which comprises three parts: header, payload, and signature. The Header typically declares the token type (JWT) and the signing algorithm (e.g., HMAC SHA256). The Payload contains the claims, which could be registered, public, or private claims. Lastly, the Signature is computed by encoding the Header and Payload using Base64URL and then signing it with a secret key.

为了理解JWT，让我们来探索它们的结构，它包括三个部分：头部（header）、负载（payload）和签名（signature）。头部通常声明了令牌类型（JWT）和签名算法（例如HMAC SHA256）。负载包含了声明，这些声明可以是注册声明、公共声明或私有声明。最后，签名是通过使用Base64URL编码头部和负载，然后使用秘密密钥进行签名计算得到的。

For instance, consider a JWT token used in a user authentication scenario:

例如，考虑在用户认证场景中使用的JWT令牌：

```java
// Header
{
  "alg": "HS256",
  "typ": "JWT"
}
// Payload
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
// Signature
HMACSHA256(
  *base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)*

```

This example illustrates a JWT token where the payload carries the subject's identity, user name, and administrative rights. The server can validate this token using the specified algorithm and secret key.

这个例子展示了一个JWT令牌，其中载荷携带了用户的身份、用户名和管理权限。服务器可以使用指定的算法和密钥验证这个令牌。
## OAuth 2.0: The Delegated Authorization Framework

## OAuth 2.0：委托授权框架


OAuth, specifically OAuth 2.0, is not a token format but an authorization framework. It defines a series of flows, or 'grant types,' which enable a client application to access resources on behalf of a user. OAuth involves obtaining an 'access token,' which the client uses to authenticate requests to a resource server.

OAuth, 特别是 OAuth 2.0，并不是一个令牌格式，而是一个授权框架。它定义了一系列的流程，或者称为“授权类型”，使得客户端应用能够代表用户访问资源。OAuth 包括获取一个“访问令牌”，客户端使用该令牌对资源服务器发起身份验证请求。

OAuth's strength is its versatility in handling different scenarios, from web applications to mobile devices and server-to-server communication. It separates the role of the client (requesting access) from the resource owner (the user) and the authorization server (validating the user and issuing tokens).

OAuth的强大之处在于其在处理不同场景时的多功能性，从网络应用到移动设备再到服务器之间的通信。它将客户端（请求访问）的角色与资源所有者（用户）和授权服务器（验证用户并发放令牌）分离。 

Translated: OAuth的強大之處在於其在處理不同場景時的多功能性，從網絡應用到移動設備再到伺服器之間的通信。它將客戶端（請求訪問）的角色與資源擁有者（用戶）和授權伺服器（驗證用戶並發放令牌）分離。

Consider a web application that uses OAuth to access a user's data from a social networking service. The flow typically involves:

考虑一个使用OAuth从社交网络服务中访问用户数据的Web应用程序。通常的流程包括：

Redirecting the user to the service's authorization page.

将用户重定向到服务的授权页面。

Upon consent, the service redirects back to the web application with an authorization code.

经过同意，服务将使用授权代码重定向回网络应用程序。

The application exchanges this code for an access token.

该应用程序通过此代码交换访问令牌。

Finally, the application uses this token to make API calls on behalf of the user.

最后，该应用程序使用此令牌代表用户进行API调用。

This process ensures that the user's credentials are not exposed to the web application, thereby enhancing security.

这个过程确保用户的凭证不会暴露给网络应用程序，从而提高安全性。
## OAuth 2.0 in Depth: Grant Types and Flows

## OAuth 2.0 深入解析：授权类型和流程


OAuth 2.0 offers various grant types for different scenarios, each designed to provide secure delegated access under specific conditions.

OAuth 2.0 提供了不同场景的各种授权类型，每种类型都旨在在特定条件下提供安全的委托访问。

Authorization Code Grant: Ideal for server-side applications, this grant type involves redirecting the user to the authorization server, obtaining an authorization code from the user, and exchanging it for an access token at the server. This process enhances security by avoiding direct exposure of tokens to the user-agent.

授权码授权：适用于服务器端应用程序，此授权类型涉及将用户重定向到授权服务器，从用户那里获得授权码，并在服务器上将其交换为访问令牌。此过程通过避免将令牌直接暴露给用户代理来增强安全性。

Implicit Grant: Tailored for clients running within a browser, this grant type simplifies the flow by directly returning an access token, skipping the authorization code exchange step. This suits applications that cannot securely store the client's secret. This is where JWTs shine, as they can be verified without server dependencies using public JWKs.

隐式授权：专为在浏览器内运行的客户端定制，这种授权类型通过直接返回访问令牌来简化流程，跳过授权码交换步骤。这适用于无法安全存储客户端密钥的应用程序。这就是JWT的亮点所在，它们可以使用公共JWK进行验证而无需依赖于服务器。

Resource Owner Password Credentials Grant: Here, the user provides a username and password directly to the application, which then exchanges them for an access token. While straightforward, this method is less secure and recommended only for trusted applications.

资源所有者密码凭证授权：在这里，用户直接向应用程序提供用户名和密码，然后应用程序用它们来交换访问令牌。虽然简单直接，但这种方法安全性较低，仅建议用于可信任的应用程序。

Client Credentials Grant: Used for server-to-server communication, this grant type allows the client to obtain an access token using its credentials. It’s ideal for scenarios where the application acts on its own behalf rather than on behalf of a user.

客户端凭证授权：用于服务器之间的通信，此授权类型允许客户端使用凭证获取访问令牌。适用于应用程序代表自己而不是代表用户的情况。
## JWTs and OAuth: Working Together

## JWTs和OAuth：共同合作

In Chinese: JWT（JSON Web Tokens）和OAuth：共同合作


Despite their differences, JWT and OAuth can work together effectively. In many OAuth implementations, the access tokens issued are, in fact, JWTs. This combination leverages both technologies' strengths: OAuth's robust authorization framework and JWT's ability to encode user information and claims securely.

尽管有所不同，JWT和OAuth可以有效地共同使用。在许多OAuth实现中，实际上是发行了JWT的访问令牌。这种组合充分利用了两种技术的优势：OAuth的强大授权框架和JWT的安全编码用户信息和声明的能力。

尽管有所不同，JWT和OAuth可以有效地共同使用。在许多OAuth实现中，实际上是发行了JWT的访问令牌。这种组合充分利用了两种技术的优势：OAuth的强大授权框架和JWT的安全编码用户信息和声明的能力。  
![](https://media.graphassets.com/resize=width:2065,height:1436/DKZK2J9eTfSLEuaHzUUZ)

For example, in an OAuth 2.0 flow, once the client receives an access token (which could be a JWT), it can make authenticated requests to the resource server. The server then validates the JWT, ensuring it’s signed and not tampered with, and extracts the user information and permissions encoded within it.

例如，在OAuth 2.0流程中，一旦客户端接收到访问令牌（可能是一个JWT），它可以向资源服务器发起经过身份验证的请求。服务器然后验证JWT，确保其签名正确且未被篡改，并提取其中编码的用户信息和权限。

This combination is particularly useful in Single Page Applications (SPAs) and mobile apps, where the stateless nature of JWTs helps maintain user sessions without server-side storage, while OAuth manages the permissions and scopes of what the client can access.

这种组合在单页面应用程序（SPAs）和移动应用程序中特别有用，在这些应用程序中，JWT的无状态性有助于在没有服务器端存储的情况下维护用户会话，而OAuth则管理客户端可以访问的权限和作用域。

Security Considerations

安全考虑

While both JWT and OAuth provide strong security mechanisms, it's critical to implement them correctly to avoid vulnerabilities:

虽然JWT和OAuth都提供了强大的安全机制，但是正确地实施它们以避免漏洞非常重要。

Securing JWT: Ensure the token is encrypted and uses a strong signing algorithm. Avoid exposing sensitive information in JWT payloads, as they can be decoded if not encrypted.

保护JWT：确保令牌被加密并使用强大的签名算法。避免在JWT负载中暴露敏感信息，因为如果不加密，则可解码。

OAuth Security: Use HTTPS for all transactions involving OAuth. Be cautious with redirecting URIs and validate them to prevent redirection attacks. Always store and handle tokens securely.

OAuth安全：在涉及OAuth的所有交易中使用HTTPS。对于重定向URI要谨慎，并验证它们以防止重定向攻击。始终安全地存储和处理令牌。

OAuth安全性：对于涉及OAuth的所有交易，请使用HTTPS。在重定向URI上要谨慎，并验证其以防止重定向攻击。始终安全地存储和处理令牌。
## JWTs and OAuth in Authorization

## JWT和OAuth在授权中的作用


Another aspect in which JWT and OAuth play an important role is authorization - the stage at which an application decides what a user is allowed or denied access to. In JWTs, token claims can provide important information about the user attributes required for permissions. In OAuth flows, the token scopes provide information about the specific token's desired scopes.

JWT和OAuth发挥重要作用的另一个方面是授权 - 应用程序决定用户被允许或拒绝访问的阶段。在JWT中，令牌声明可以提供有关所需权限的用户属性的重要信息。在OAuth流程中，令牌范围提供有关特定令牌所需范围的信息。

One common misconception regarding JWT and OAuth is their ability to be used as a comprehensive application authorization service. Developers often query the scopes and claims directly in the applications to determine if a user can or cannot perform particular actions. This approach can lead to some serious issues:

一个关于JWT和OAuth的常见误解是它们能够用作全面的应用授权服务。开发人员通常直接查询应用程序中的范围和声明，以确定用户是否能够执行特定操作。这种方法可能会导致一些严重的问题。

To tackle these challenges, scopes and claims must be used in an authorization service that decouples policy from code. An authorization service, Such as Permit.io, should evaluate authorization decisions using scopes and claims as part of a comprehensive permission model that calculates all relevant security factors, allowing you to integrate JWTs and OAuth into your application seamlessly.

为了应对这些挑战，授权服务必须使用作用域和声明来将策略与代码解耦。授权服务，如Permit.io，应该使用作用域和声明来评估授权决策，作为一个综合的权限模型的一部分，计算所有相关的安全因素，使您可以将JWT和OAuth无缝集成到您的应用程序中。
## Conclusion

## 结论


Understanding OAuth and JWT is essential for modern web development. While OAuth provides a flexible authorization framework, JWT offers a compact way to represent user information securely. Combined, they form a potent combination for securing web applications, providing strong authentication and fine-grained access control.

了解OAuth和JWT对于现代Web开发至关重要。虽然OAuth提供了一个灵活的授权框架，但JWT提供了一种安全地表示用户信息的紧凑方式。结合起来，它们为保护Web应用程序提供了强大的身份验证和细粒度访问控制的有力组合。

了解OAuth和JWT对于现代Web开发至关重要。虽然OAuth提供了一个灵活的授权框架，但JWT提供了一种安全地表示用户信息的紧凑方式。结合起来，它们为保护Web应用程序提供了强大的身份验证和细粒度访问控制的有力组合。