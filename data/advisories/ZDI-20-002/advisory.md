# ZDI-20-002: (0Day) Microsoft Outlook HTML Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-002
- **ZDI-CAN:** ZDI-CAN-9608
- **Date:** 2020-01-02
- **CVE:** N/A
- **CVSS:** 3.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Outlook
- **Credit:** asnine
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-002/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Outlook. User interaction is required to exploit this vulnerability in that the target must open an email. The specific flaw exists within the handling of HTML. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 12/17/2019 – ZDI disclosed the report to the vendor 12/17/2019 – The vendor acknowledged the report 12/18/2019 – The vendor provided a tracking # 12/23/2019 – The vendor advised the ZDI that “We determined your finding is valid but does not meet our bar for immediate servicing.” 12/26/2019 – ZDI requested clarification 12/26/2019 – The vendor replied that the report is an OOB read (and they are providing security servicing OOB writes) 12/30/2019 - ZDI notified the vendor the intention to publish as 0-day -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2019-12-17 - Vulnerability reported to vendor
- 2020-01-02 - Coordinated public release of advisory
