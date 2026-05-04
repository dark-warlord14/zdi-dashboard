# ZDI-23-1580: (0Day) Microsoft Exchange DownloadDataFromOfficeMarketPlace Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1580
- **ZDI-CAN:** ZDI-CAN-22100
- **Date:** 2023-11-02
- **CVE:** N/A
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1580/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the DownloadDataFromOfficeMarketPlace method. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the Exchange server.

## Additional Details

09/08/23 – ZDI reported the vulnerability to the vendor. 09/11/23 – The vendor acknowledged the report. 09/20/23 – The vendor states that the vulnerability does not require immediate servicing. 09/29/23 – ZDI informed the vendor that we are publishing this case as a zero-day advisory in the coming weeks. 11/01/02 – ZDI Informed the vendor that we intend to publish on 11/02/2023. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-09-08 - Vulnerability reported to vendor
- 2023-11-02 - Coordinated public release of advisory
