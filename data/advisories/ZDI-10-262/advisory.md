# ZDI-10-262: Apple QuickTime PICT directBitsRect Pack3 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-262
- **ZDI-CAN:** ZDI-CAN-977
- **Date:** 2010-12-07
- **CVE:** CVE-2010-3800
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Moritz Jodeit of n.runs AG
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-262/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses directBitsRect records within a .pict file. When decompressing data within this structure, the application will allocate space for the target buffer using fields described within the file and then use a different length to decompress the total data from the file. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-11-05 - Vulnerability reported to vendor
- 2010-12-07 - Coordinated public release of advisory
