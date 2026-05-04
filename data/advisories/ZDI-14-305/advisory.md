# ZDI-14-305: Hewlett-Packard Network Node Manager ovopi.dll Stack Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-305
- **ZDI-CAN:** ZDI-CAN-2264
- **Date:** 2014-09-16
- **CVE:** CVE-2014-2624
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Network Node Manager
- **Credit:** d(-_-)b HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-305/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Network Node Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within ovopi.dll which listens by default on UDP port 696. When parsing option -S with a buffer followed by a semi-colon, the process blindly copies user supplied data into a fixed-length buffer. A remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04378450

## Disclosure Timeline

- 2014-05-16 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory
