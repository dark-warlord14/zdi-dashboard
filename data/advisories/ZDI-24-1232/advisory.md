# ZDI-24-1232: Cohesive Networks VNS3 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1232
- **ZDI-CAN:** ZDI-CAN-24177
- **Date:** 2024-09-17
- **CVE:** CVE-2024-8808
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cohesive Networks
- **Affected Products:** VNS3
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1232/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cohesive Networks VNS3. Authentication is required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 8000 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cohesive Networks has issued an update to correct this vulnerability. More details can be found at: https://cohesive.net/support/security-responses/

## Disclosure Timeline

- 2024-07-25 - Vulnerability reported to vendor
- 2024-09-17 - Coordinated public release of advisory
- 2024-09-17 - Advisory Updated
