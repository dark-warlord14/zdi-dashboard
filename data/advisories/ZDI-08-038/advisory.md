# ZDI-08-038: Apple QuickTime SMIL qtnext Redirect File Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-038
- **ZDI-CAN:** ZDI-CAN-326
- **Date:** 2008-06-10
- **CVE:** CVE-2008-1585
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Petko D. (pdp) Petkov | GNUCITIZEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists in the handling of SMIL text embedded in video formats. No sanity checking is performed on values of the qt:next attribute. When the URI for this attribute is a file type not recognized by QuickTime, it is passed to url.dll!FileProtocolHandler which will allow explorer.exe handle non-http filetypes. Successful exploitation can result in the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2008-05-08 - Vulnerability reported to vendor
- 2008-06-10 - Coordinated public release of advisory
