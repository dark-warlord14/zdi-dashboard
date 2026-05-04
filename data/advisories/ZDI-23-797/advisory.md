# ZDI-23-797: Delta Electronics CNCSoft-B DOPSoft DPA File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-797
- **ZDI-CAN:** ZDI-CAN-19326
- **Date:** 2023-06-01
- **CVE:** CVE-2023-25177
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** CNCSoft-B
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-797/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics CNCSoft-B. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DPA files by the DOPSoft component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-157-01

## Disclosure Timeline

- 2022-11-11 - Vulnerability reported to vendor
- 2023-06-01 - Coordinated public release of advisory
- 2023-06-06 - Advisory Updated
