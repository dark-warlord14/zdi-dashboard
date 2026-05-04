# ZDI-18-245: Microsoft Windows Palette Object Race Condition Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-245
- **ZDI-CAN:** ZDI-CAN-5445
- **Date:** 2018-03-19
- **CVE:** CVE-2018-0815
- **CVSS:** 5.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:N/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-245/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32k.sys driver. During creation of a palette object, a race condition exists due to the failure to lock an object in memory between operations. An attacker can leverage this vulnerability to disclose sensitive information under the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0815

## Disclosure Timeline

- 2017-12-01 - Vulnerability reported to vendor
- 2018-03-19 - Coordinated public release of advisory
- 2018-03-19 - Advisory Updated
