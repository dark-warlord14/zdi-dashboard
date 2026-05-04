# ZDI-10-294: Rocket U2 Uni RPC Service Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-294
- **ZDI-CAN:** ZDI-CAN-368
- **Date:** 2010-12-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Rocket
- **Affected Products:** U2
- **Credit:** Ruben Santamarta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-294/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of multiple products from multiple vendors that utilize the Uni RPC protocol. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Uni RPC service (unirpcd.exe) which listens by default on TCP port 31438. The unirpc32.dll module implements an RPC protocol and is used by the Uni RPC service. While parsing a size value from an RPC packet header, an integer can overflow and consequently bypass a signed comparison. This controlled value is then used as the number of bytes to receive into a static heap buffer. By providing a specially crafted request, this heap buffer can overflow leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

Rocket U2 states that this issue was first fixed in: UniVerse 10.3.9 and UniData 7.2.8. Recommended fix pack version: UniVerse 10.3.9 and above or UniData 7.2.8 and above. Please contact your software partner or U2BC@rs.com to obtain a fixed version for UCC-676.

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-12-23 - Coordinated public release of advisory
