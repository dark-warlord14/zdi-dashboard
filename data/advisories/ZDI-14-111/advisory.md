# ZDI-14-111: Oracle Data Quality LoaderWizard ActiveX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-111
- **ZDI-CAN:** ZDI-CAN-2019
- **Date:** 2014-04-21
- **CVE:** CVE-2014-2407
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Data Quality
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-111/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Data Quality. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the TSS12.LoaderWizard.lwctrl ActiveX control. The issue lies in the failure to properly initialize values leading to a use-after-free condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2014-1972952.html

## Disclosure Timeline

- 2013-11-06 - Vulnerability reported to vendor
- 2014-04-21 - Coordinated public release of advisory
