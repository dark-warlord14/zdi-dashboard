# ZDI-24-867: (Pwn2Own) Phoenix Contact CHARX SEC-3100 CharxUpdateAgent Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-867
- **ZDI-CAN:** ZDI-CAN-24096
- **Date:** 2024-06-21
- **CVE:** CVE-2024-25994
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** NCC Group EDG (@nccgroupinfosec @_mccaulay @alexjplaskett)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-867/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create arbitrary files on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CharxUpdateAgent service, which listens on TCP port 9999 by default. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-011/

## Disclosure Timeline

- 2024-05-02 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
