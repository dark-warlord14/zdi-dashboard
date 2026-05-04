# ZDI-19-1034: (0Day) WECON PLC Editor PLCDataCeter Port Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1034
- **ZDI-CAN:** ZDI-CAN-9123
- **Date:** 2019-12-30
- **CVE:** CVE-2019-18236
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** PLC Editor
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WECON PLC Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WCP files. A crafted Port element in a WCP file can trigger an overflow of a fixed-length buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 08/08/2019 - ZDI reported the Vulnerability to ICS-CERT 08/14/2019 - ICS-CERT acknowledged the report and provided an ICS-VU# 12/13/2019 - ZDI requested any available update 12/18/2019 - ZDI advised ICS-CERT of the intention to publish the report as 0-day on 12/30/2019 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2019-08-09 - Vulnerability reported to vendor
- 2019-12-30 - Coordinated public release of advisory
