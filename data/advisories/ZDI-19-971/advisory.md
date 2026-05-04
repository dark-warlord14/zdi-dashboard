# ZDI-19-971: Fuji Electric V-Server VPR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-971
- **ZDI-CAN:** ZDI-CAN-8932
- **Date:** 2019-11-11
- **CVE:** CVE-2019-18240
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** V-Server
- **Credit:** kimiya of 9SG
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-971/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric V-Server. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of VPR files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-311-02

## Disclosure Timeline

- 2019-07-11 - Vulnerability reported to vendor
- 2019-11-11 - Coordinated public release of advisory
