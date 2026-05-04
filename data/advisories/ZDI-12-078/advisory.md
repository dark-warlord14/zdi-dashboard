# ZDI-12-078: Apple QuickTime SVQ3 Codec mb_skip_run Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-078
- **ZDI-CAN:** ZDI-CAN-1440
- **Date:** 2012-06-06
- **CVE:** CVE-2012-0669
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-078/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Apple QuickTime handles file with the Sorenson v3 Codec. When parsing the data inside the svq3 stream QuickTime does not verify the value for the mb_skip_run value it reads from the data. This value is used later as a loop counter to write data to a heap allocation without boundary checking. This can result in a heap based buffer overflow that can result in remote code execution under the context of the user running the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5261

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
