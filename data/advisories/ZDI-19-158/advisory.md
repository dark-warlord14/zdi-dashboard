# ZDI-19-158: Bitdefender SafePay openFile Arbitrary File Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-158
- **ZDI-CAN:** ZDI-CAN-7247
- **Date:** 2019-01-29
- **CVE:** CVE-2019-6737
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bitdefender
- **Affected Products:** SafePay
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-158/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender SafePay. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of TIScript. The issue lies in the handling of the openFile method, which allows for an arbitrary file write with attacker controlled data. An attacker can leverage this vulnerability execute code in the context of the current process.

## Additional Details

This issue was resolved with 23.0.11.44.

## Disclosure Timeline

- 2018-09-19 - Vulnerability reported to vendor
- 2019-01-29 - Coordinated public release of advisory
