# ZDI-15-012: Microsoft Windows WM_SYSTIMER Kernel Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-012
- **ZDI-CAN:** ZDI-CAN-2549
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0003
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-012/
## Vulnerability Details

This vulnerability allows local attackers to elevate to System privileges on vulnerable installations of Microsoft Windows. This vulnerability requires the ability to run arbitrary unprivileged code. The specific flaw exists within the handling of the WM_SYSTIMER message. By malforming the window handle in the message, an attacker is able to cause the kernel to write to a controlled address. An attacker could leverage this to execute arbitrary code in the context of the System.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-010

## Disclosure Timeline

- 2014-10-09 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
