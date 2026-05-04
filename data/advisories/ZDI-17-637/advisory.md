# ZDI-17-637: Microsoft Edge XAML File Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-637
- **ZDI-CAN:** ZDI-CAN-4461
- **Date:** 2017-08-08
- **CVE:** CVE-2017-8503
- **CVSS:** 3.7
- **CVSS Vector:** AV:L/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Thomas Vanhoutte
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-637/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Microsoft Edge. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of XAML files. When an XAML file is downloaded, Microsoft Edge does not set appropriate file permissions. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8503

## Disclosure Timeline

- 2017-02-01 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
