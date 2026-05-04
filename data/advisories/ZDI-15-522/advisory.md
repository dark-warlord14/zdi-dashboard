# ZDI-15-522: Microsoft Internet Explorer EditWith Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-522
- **ZDI-CAN:** ZDI-CAN-3042
- **Date:** 2015-10-13
- **CVE:** CVE-2015-6047
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-522/
## Vulnerability Details

This vulnerability allows remote attackers to escape the Application Container and execute code in the context of the logged-in user on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the EditWith functionality of the broker process for Internet Explorer. Code that is running in the AppContainer can use the DelegateExecute functionality of shell execution to execute arbitrary applications in the context of the user, not just applications that are in the Internet Explorer allowed list.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-106

## Disclosure Timeline

- 2015-07-07 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
