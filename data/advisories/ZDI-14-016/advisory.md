# ZDI-14-016: GE Proficy CIMPLICITY CimWebServer File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-016
- **ZDI-CAN:** ZDI-CAN-1623
- **Date:** 2014-02-13
- **CVE:** CVE-2014-0751
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** GE
- **Affected Products:** Proficy CIMPLICITY
- **Credit:** ZombiE and amisto0x07
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-016/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE Proficy CIMPLICITY. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CimWebServer component. This component performs insufficient parameter validation on the szScreen field. Successful exploitation will allow an attacker to upload and execute an arbitrary file on the target server.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-023-01

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2014-02-13 - Coordinated public release of advisory
