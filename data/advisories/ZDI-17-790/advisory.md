# ZDI-17-790: Trend Micro Mobile Security for Enterprise upload_font_file Unrestricted File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-790
- **ZDI-CAN:** ZDI-CAN-4785
- **Date:** 2017-09-15
- **CVE:** CVE-2017-14079
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Mobile Security for Enterprise
- **Credit:** Steven Seeley (mr_me) of Offensive Security & Roberto Suggi Liverani - @malerisch - http://blog.malerisch.net/
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-790/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Mobile Security for Enterprise. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of the upload_font_file action. The issue results from the lack of proper validation of user-supplied data, which can allow for the upload of arbitrary files. An attacker can leverage this vulnerability to execute arbitrary code under the context of the IUSR account.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1118224

## Disclosure Timeline

- 2017-05-16 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
