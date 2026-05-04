# ZDI-14-173: OpenSSL DTLS Fragment Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-173
- **ZDI-CAN:** ZDI-CAN-2304
- **Date:** 2014-06-05
- **CVE:** CVE-2014-0195
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** OpenSSL
- **Affected Products:** OpenSSL
- **Credit:** Jüri Aedla
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-173/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OpenSSL. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of DTLS packets. The issue lies in the assumption that all fragments specify the same message size. An attacker could leverage this vulnerability to execute code in the context of the process using OpenSSL.

## Additional Details

OpenSSL has issued an update to correct this vulnerability. More details can be found at: https://www.openssl.org/news/secadv_20140605.txt

## Disclosure Timeline

- 2014-04-22 - Vulnerability reported to vendor
- 2014-06-05 - Coordinated public release of advisory
