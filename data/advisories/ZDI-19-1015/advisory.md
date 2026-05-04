# ZDI-19-1015: (0Day) WECON PLC Editor WCP File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1015
- **ZDI-CAN:** ZDI-CAN-8456
- **Date:** 2019-12-12
- **CVE:** CVE-2019-18236
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** PLC Editor
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1015/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Wecon PLC Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WCP files. When parsing the project version attribute, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 06/13/19 - ZDI submitted the vulnerability report to ICS-CERT 07/09/19 - ICS-CERT replied with an ICS-VU# and acknowledgement that they sent the report to the vendor 09/13/19 - ZDI requested an update 09/30/19 - ICS-CERT replied that they last communicated with the vendor on 08/24/19 and that they were working on it 11/29/19 - ZDI requested an update 12/06/19 - ZDI notified ICS-CERT that the report will be published as 0-day on 12/12/19 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2019-06-13 - Vulnerability reported to vendor
- 2019-12-12 - Coordinated public release of advisory
