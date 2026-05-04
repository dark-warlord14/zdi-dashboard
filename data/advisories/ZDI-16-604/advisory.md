# ZDI-16-604: IBHsoftec S7-SoftPLC CPX43 Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-604
- **ZDI-CAN:** ZDI-CAN-3832
- **Date:** 2016-11-08
- **CVE:** CVE-2016-8364
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBHsoftec
- **Affected Products:** S7-SoftPLC
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-604/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBHsoftec SoftPLC. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of packets by the service listening on TCP port 502. The issue lies in the failure to properly validate the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of Administrator.

## Additional Details

IBHsoftec has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-306-02

## Disclosure Timeline

- 2016-07-12 - Vulnerability reported to vendor
- 2016-11-08 - Coordinated public release of advisory
