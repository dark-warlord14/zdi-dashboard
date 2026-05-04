# ZDI-10-068: Apple QuickTime H.263 Array Index Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-068
- **ZDI-CAN:** ZDI-CAN-692
- **Date:** 2010-04-09
- **CVE:** CVE-2010-0062
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-068/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required in that a target must open a malicious media file or visit a malicious page. The specific flaw exists within the parsing of H.263 media files. The code within QuickTime trusts various values from MDAT structures and uses them during operations on heap memory. By crafting specific values the corruption can be leveraged to execute remote code under the context of the user running the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4104

## Disclosure Timeline

- 2010-04-06 - Vulnerability reported to vendor
- 2010-04-09 - Coordinated public release of advisory
