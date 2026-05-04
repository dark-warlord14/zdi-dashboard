# ZDI-11-108: Mac OS X Compact Font Format Decoder Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-108
- **ZDI-CAN:** ZDI-CAN-860
- **Date:** 2011-03-22
- **CVE:** CVE-2011-0176
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Preview
- **Credit:** geekable
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-108/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mac OS X's CFF Decoder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the Type1Scaler library processes a specially formatted compact font file. When processing this file, the application will corrupt memory outside the bounds of an allocated buffer. This can lead to code execution under the context of the application that utilizes the library.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4581

## Disclosure Timeline

- 2010-12-01 - Vulnerability reported to vendor
- 2011-03-22 - Coordinated public release of advisory
