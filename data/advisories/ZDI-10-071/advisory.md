# ZDI-10-071: Adobe Reader TrueType Font Handling Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-071
- **ZDI-CAN:** ZDI-CAN-696
- **Date:** 2010-04-13
- **CVE:** CVE-2010-0195
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-071/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe's Acrobat Reader. User interaction is required in that the victim must be coerced into opening a malicious document or visiting a malicious URL. The specific flaw exists within the parsing of embedded fonts inside a PDF document. Upon parsing particular tables out of a font file the application will miscalculate an index used for seeking into a buffer. Later the application will begin to copy data into the calculated pointer corrupting the referenced data structure. Successful exploitation will lead to code execution under the context of the application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-09.html

## Disclosure Timeline

- 2010-02-18 - Vulnerability reported to vendor
- 2010-04-13 - Coordinated public release of advisory
