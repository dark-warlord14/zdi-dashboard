# ZDI-20-487: Eaton HMiSoft VU3 File Parsing LinkSize Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-487
- **ZDI-CAN:** ZDI-CAN-10166
- **Date:** 2020-04-15
- **CVE:** CVE-2020-10639
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Eaton
- **Affected Products:** HMiSoft
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-487/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Eaton HMiSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the LinkSize field. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Eaton has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-105-01

## Disclosure Timeline

- 2020-02-07 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
