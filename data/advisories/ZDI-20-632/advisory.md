# ZDI-20-632: Advantech WebAccess IOCTL 0x2711 bwscrp Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-632
- **ZDI-CAN:** ZDI-CAN-10325
- **Date:** 2020-05-08
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-632/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within bwscrp.exe when invoked via IOCTL 0x2711. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-128-36

## Disclosure Timeline

- 2020-02-21 - Vulnerability reported to vendor
- 2020-05-08 - Coordinated public release of advisory
