# ZDI-13-143: Microsoft Internet Explorer jsdbgui Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-143
- **ZDI-CAN:** ZDI-CAN-1806
- **Date:** 2013-06-27
- **CVE:** CVE-2013-3126
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-143/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of strings in the Javascript console. By manipulating string objects an attacker can force a sign-extension bug to occur. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms13-047

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
