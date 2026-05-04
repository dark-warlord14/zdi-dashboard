# ZDI-14-054: Schneider Electric OPC Factory Server OFS Client Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-054
- **ZDI-CAN:** ZDI-CAN-1881
- **Date:** 2014-04-03
- **CVE:** CVE-2014-0774
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Schneider Electric
- **Affected Products:** OPC Factory Server
- **Credit:** 0x7A240E67
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-054/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Schneider Electric OFS Client. User interaction is required to exploit this vulnerability in that the target must load a malicious file. The specific flaw exists within the parsing of the configuration file. A crafted configuration file will result in an exploitable stack buffer overflow. An attacker can use this to execute arbitrary code in the context of the OFS Client.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-058-02

## Disclosure Timeline

- 2014-01-13 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
