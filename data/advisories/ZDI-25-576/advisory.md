# ZDI-25-576: Siemens SINEC NMS uploadFWBinary Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-576
- **ZDI-CAN:** ZDI-CAN-26572
- **Date:** 2025-07-08
- **CVE:** CVE-2025-40738
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** SINEC NMS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-576/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens SINEC NMS. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the uploadFWBinary method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of LOCAL SERVICE.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-078892.html

## Disclosure Timeline

- 2025-04-10 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated
