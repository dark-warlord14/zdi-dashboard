# ZDI-19-1032: (0Day) WECON PIStudio HSC File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1032
- **ZDI-CAN:** ZDI-CAN-8927
- **Date:** 2019-12-30
- **CVE:** CVE-2018-14810
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** PIStudio
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WECON PIStudio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of HSC files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 06/26/2019 - ZDI provided the vulnerability report to ICS-CERT 07/02/2019 - ICS-CERT acknowledged the report and provided an ICS VU# 11/19/2019 - ZDI requested any available update 11/29/2019 - ZDI requested any available update 12/05/2019 - ZDI requested any available update 12/18/2019 - ZDI advised ICS-CERT of the intention to publish the report as 0-day on Dec 30 12/02/2021 - The vendor published an update https://us-cert.cisa.gov/ics/advisories/ICSA-18-277-01 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2019-06-26 - Vulnerability reported to vendor
- 2019-12-30 - Coordinated public release of advisory
- 2021-12-03 - Advisory Updated
