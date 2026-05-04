# ZDI-19-149: (0Day) Wecon LeviStudioU screendata Desc FigureFile Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-149
- **ZDI-CAN:** ZDI-CAN-6516
- **Date:** 2019-01-29
- **CVE:** CVE-2019-6539
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** LeviStudioU
- **Credit:** Ziad Badawi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-149/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HSC files. When parsing the Desc and FigureFile attributes, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/12/18 – ZDI provided the reports to ICS-CERT 08/16/18 – ICS-CERT provided an ICS-VU# 11/15/18 – ZDI requested any update from ICS-CERT 11/26/18 – ZDI requested any update from ICS-CERT 12/07/18 – ZDI requested any update from ICS-CERT 01/09/19 – ZDI advised ICS-CERT of the intention to 0-day publish 01/25/19 – ZDI telephoned ICS-CERT to discuss status and 0-day publish -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-07-25 - Vulnerability reported to vendor
- 2019-01-29 - Coordinated public release of advisory
- 2019-05-30 - Advisory Updated
