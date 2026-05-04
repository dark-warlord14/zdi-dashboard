# ZDI-19-820: Fuji Electric Alpha5 WPA File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-820
- **ZDI-CAN:** ZDI-CAN-8590
- **Date:** 2019-09-11
- **CVE:** CVE-2019-13520
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha5
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-820/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Alpha5. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WPA files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-227-02

## Disclosure Timeline

- 2019-05-31 - Vulnerability reported to vendor
- 2019-09-11 - Coordinated public release of advisory
