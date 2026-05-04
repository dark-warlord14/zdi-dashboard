# ZDI-21-879: (0Day) WSO2 API Manager JMX Use of Hard-coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-879
- **ZDI-CAN:** ZDI-CAN-13449
- **Date:** 2021-07-19
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** WSO2
- **Affected Products:** API Manager
- **Credit:** Lukasz Wierzbicki
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-879/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WSO2 API Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the JMX RMI service, which listens on TCP port 11111 by default. The service contains a hard-coded password for the administrator user. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/26/21 – ZDI reported the vulnerability to the vendor 05/28/21 – The vendor acknowledged the report 06/06/21 – The vendor claimed that the issue does not have a security impact 06/07/21 – ZDI provided additional evidence 07/05/21 – The vendor communicated that they won’t fix the issue 07/09/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 07/19/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-05-26 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
