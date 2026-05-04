# ZDI-11-082: Oracle Java Runtime NTLM Authentication Information Leakage Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-082
- **ZDI-CAN:** ZDI-CAN-552
- **Date:** 2011-02-15
- **CVE:** CVE-2010-4466
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Sami Koivu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-082/
## Vulnerability Details

This vulnerability allows remote attackers to leak authentication details on vulnerable installations of the Oracle Java Runtime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of NTLM authentication requested generated in the context of the Java Runtime. The Java Virtual Machine will ignore browser policies and respond to WWW-Authenticate requests from the Internet zone resulting in the leakage of NTLM authentication hashes to attackers.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2011-304611.html

## Disclosure Timeline

- 2009-08-20 - Vulnerability reported to vendor
- 2011-02-15 - Coordinated public release of advisory
