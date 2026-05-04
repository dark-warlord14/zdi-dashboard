# ZDI-15-386: Microsoft Internet Explorer HelpPane Sandbox Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-386
- **ZDI-CAN:** ZDI-CAN-2923
- **Date:** 2015-08-11
- **CVE:** CVE-2015-2454
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Ashutosh Mehra (https://twitter.com/ashutoshmehra)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-386/
## Vulnerability Details

This vulnerability allows remote attackers to escape Protected Mode on vulnerable installations of Microsoft Internet Explorer User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the HelpPane executable. The issue lies in the validation of the integrity level of the COM client, which is performed with a comparison against the integrity level of the desktop's shell. An attacker can leverage this vulnerability to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-080

## Disclosure Timeline

- 2015-05-07 - Vulnerability reported to vendor
- 2015-08-11 - Coordinated public release of advisory
