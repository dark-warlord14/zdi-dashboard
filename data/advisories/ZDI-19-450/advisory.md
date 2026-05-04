# ZDI-19-450: (0Day) Wecon PIStudio HSC File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-450
- **ZDI-CAN:** ZDI-CAN-7641
- **Date:** 2019-05-02
- **CVE:** CVE-2018-14810
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** PIStudio
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-450/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon PIStudio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of HSC files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/11/2018 - ZDI disclosed the report to ICS-CERT 02/21/2019 - ZDI wrote to ICS-CERT to indicate that there had been no reply to the report and ZDI re-sent the report 03/11/2019 - ICS-CERT advised ZDI that the vendor had verified that they received the reports and were in the process of validating these 04/01/2019 - ZDI wrote to ICS-CERT "Can you please confirm when this report was provided to the vendor?" 04/19/2019 - ZDI advised ICS-CERT of the intent to publish the report as 0-day on 05/02/2019 12/02/2021 - The vendor published an update https://us-cert.cisa.gov/ics/advisories/ICSA-18-277-01 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-12-11 - Vulnerability reported to vendor
- 2019-05-02 - Coordinated public release of advisory
- 2021-12-03 - Advisory Updated
