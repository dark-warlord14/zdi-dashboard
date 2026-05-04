# ZDI-26-058: AzeoTech DAQFactory Pro CTL File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-058
- **ZDI-CAN:** ZDI-CAN-27641
- **Date:** 2026-02-03
- **CVE:** CVE-2025-66589
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** AzeoTech
- **Affected Products:** DAQFactory
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-058/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of AzeoTech DAQFactory. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CTL files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

AzeoTech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-345-03

## Disclosure Timeline

- 2025-09-11 - Vulnerability reported to vendor
- 2026-02-03 - Coordinated public release of advisory
- 2026-02-03 - Advisory Updated
