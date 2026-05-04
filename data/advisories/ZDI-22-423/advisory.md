# ZDI-22-423: (0Day) Delta Industrial Automation DIAEnergie HandlerPage_KID Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-423
- **ZDI-CAN:** ZDI-CAN-15580
- **Date:** 2022-03-01
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** DIAEnergie
- **Credit:** Dusan Stevanovic from Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-423/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Industrial Automation DIAEnergie. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the HandlerPage_KID endpoint. The issue results from the lack of proper validation of user-supplied data, which can allow the upload of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of web server.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/13/21 – ZDI reported the vulnerability to ICS-CERT 01/12/22 – ZDI requested an update 02/18/22 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 02/28/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-10-13 - Vulnerability reported to vendor
- 2022-03-01 - Coordinated public release of advisory
- 2022-03-30 - Advisory Updated
