# ZDI-14-060: EMC Connectrix Manager Converged Network Edition inmservlets.war FileUploadController Servlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-060
- **ZDI-CAN:** ZDI-CAN-2133
- **Date:** 2014-04-08
- **CVE:** CVE-2014-2276
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** EMC
- **Affected Products:** Connectrix Manager Converged Network Edition
- **Credit:** Bluesea
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-060/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary files on vulnerable installations of EMC Connectrix Manager Converged Network Edition. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FileUploadController servlet which is part of inmservlets. This vulnerability allows an unauthenticated user to read an arbitrary file on the system. An attacker can use this to either disclose sensitive data or to disclose information about the server that can be used in a subsequent attack.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/bugtraq/2014/Mar/att-114/ESA-2014-018.txt

## Disclosure Timeline

- 2014-02-10 - Vulnerability reported to vendor
- 2014-04-08 - Coordinated public release of advisory
