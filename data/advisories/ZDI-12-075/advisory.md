# ZDI-12-075: Apple QuickTime RLE Sample Decoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-075
- **ZDI-CAN:** ZDI-CAN-1370
- **Date:** 2012-06-06
- **CVE:** CVE-2012-0668
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Luigi Auriemma Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-075/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application decodes video samples encoded with the RLE codec. When decompressing the sample, the application will fail to accommodate for the canvas the sample is rendered into. This can cause a buffer overflow and thus can be taken advantage of in order to gain code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5261

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
