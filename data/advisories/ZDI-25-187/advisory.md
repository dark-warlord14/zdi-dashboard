# ZDI-25-187: (0Day) BEC Technologies Multiple Routers sys ping Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-187
- **ZDI-CAN:** ZDI-CAN-25903
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2773
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** BEC Technologies
- **Affected Products:** Multiple Routers
- **Credit:** Steven C Yu of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-187/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of BEC Technologies Multiple Routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the management interface, which listens on TCP port 22 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

12/06/24 – ZDI contacted the vendor’s support team via email 02/13/25 – ZDI requested an update 03/12/25 – ZDI informed the vendor that since we have not received a response, we will publish the report as a 0-day advisory 03/25/25 - ZDI published the report as a 0-day advisory 11/20/25 - The vendor notified ZDI that the vulnerability has been patched Mitigation: For all firmware versions 1.04.1.x, update to 1.04.1.676 or later. For all firmware versions 1.00.1.x, update to 1.00.1.196 or later.

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-11-24 - Advisory Updated
