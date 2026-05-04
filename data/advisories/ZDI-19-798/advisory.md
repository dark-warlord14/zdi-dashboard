# ZDI-19-798: Fuji Electric Alpha5 SDP File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-798
- **ZDI-CAN:** ZDI-CAN-8566
- **Date:** 2019-09-05
- **CVE:** CVE-2019-13520
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha5
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-798/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Alpha5. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SDP files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the Administrator.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-227-02

## Disclosure Timeline

- 2019-05-18 - Vulnerability reported to vendor
- 2019-09-05 - Coordinated public release of advisory
