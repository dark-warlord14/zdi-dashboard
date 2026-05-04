# ZDI-21-517: (0Day) Delta Industrial Automation DOPSoft DPA File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-517
- **ZDI-CAN:** ZDI-CAN-12647
- **Date:** 2021-05-06
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DOPSoft
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-517/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation DOPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPA files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/13/21 – ZDI reported the vulnerability to ICS-CERT 01/15/21 – ICS-CERT acknowledged the report 04/29/21 – ICS-CERT indicated the vendor had delayed the release until the end of June 04/29/20 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 05/06/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-01-13 - Vulnerability reported to vendor
- 2021-05-06 - Coordinated public release of advisory
