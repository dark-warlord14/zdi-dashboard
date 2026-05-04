# ZDI-20-001: (0Day) Microsoft Windows Media Player Mpeg Audio Codec Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-001
- **ZDI-CAN:** ZDI-CAN-8185
- **Date:** 2020-01-02
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Player
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-001/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Windows Media Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the MPEG audio codec. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 08/13/2019 – ZDI disclosed the report to the vendor and the vendor acknowledged 08/14/2019 – The vendor provided a case number 08/27/2019 – The vendor provided an ‘in assessment’ status update 08/29/2019 – The vendor notified the ZDI that they were not able to reproduce the report 08/30/2019 – ZDI provided additional settings information 09/03/2019 – The vendor notified the ZDI that they were not able to reproduce the report and requested an additional step 09/04/2019 – ZDI posed clarifying questions 09/12/2019 – The vendor replied 09/17/2019 – ZDI provided a crash dump 10/01/2019 – The vendor provided an ‘in development’ status update 12/05/2019 - ZDI and the vendor had a call regarding this and other reports and ZDI was told to expect a rebuttal/no fix reply 12/18/2019 – ZDI requested any available update 12/23/2019 – The vendor advised the ZDI that the report does not meet the bar for servicing 12/27/2019 - ZDI notified the vendor the intention to publish as 0-day -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2020-01-02 - Coordinated public release of advisory
