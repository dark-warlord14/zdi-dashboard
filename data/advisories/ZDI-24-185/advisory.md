# ZDI-24-185: Inductive Automation Ignition getJavaExecutable Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-185
- **ZDI-CAN:** ZDI-CAN-22029
- **Date:** 2024-02-21
- **CVE:** CVE-2023-50233
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-185/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. User interaction is required to exploit this vulnerability in that the target must connect to a malicious server. The specific flaw exists within the getJavaExecutable method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://security.inductiveautomation.com/?tcuUid=fc4c4515-046d-4365-b688-693337449c5b

## Disclosure Timeline

- 2023-08-29 - Vulnerability reported to vendor
- 2024-02-21 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
