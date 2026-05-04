# ZDI-21-876: (0Day) Advantech WebAccess/NMS DashBoardAction Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-876
- **ZDI-CAN:** ZDI-CAN-11883
- **Date:** 2021-07-19
- **CVE:** CVE-2021-32951
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** Selim Enes Karaduman (@Enesdex)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-876/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WebAccess/NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the DashBoardAction endpoint of the web server. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose information from the application.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/03/21 – ZDI reported the vulnerability to ICS-CERT 03/03/21 – ICS-CERT acknowledged the report 07/05/21 – ZDI requested an update 07/08/21 – ZDI requested an update 07/09/21 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 07/19/21 08/17/21 - ICS-CERT published an advisory https://us-cert.cisa.gov/ics/advisories/icsa-21-229-02 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-03-03 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
- 2021-08-25 - Advisory Updated
