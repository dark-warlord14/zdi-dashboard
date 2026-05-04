# ZDI-11-286: Novell Groupwise Client DOCX Loader Relationship Id Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-286
- **ZDI-CAN:** ZDI-CAN-966
- **Date:** 2011-10-14
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Groupwise
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-286/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Groupwise Client. User interaction is required to exploit this vulnerability in that the target must open a malicious e-mail message. The specific flaw exists within the component responsible for parsing DOCX attachment files. When handling the "Relationship Id" field within such a file, the process copies the contents into a static buffer on the stack. By supplying a large enough value this buffer can be overflowed leading to arbitrary code execution under the context of the user running the mail client.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?usemicrosite=true&searchString=7009207

## Disclosure Timeline

- 2010-11-30 - Vulnerability reported to vendor
- 2011-10-14 - Coordinated public release of advisory
