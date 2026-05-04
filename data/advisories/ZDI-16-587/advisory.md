# ZDI-16-587: Hewlett Packard Enterprise System Management Homepage SetSMHData Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-587
- **ZDI-CAN:** ZDI-CAN-3722
- **Date:** 2016-11-02
- **CVE:** CVE-2016-4395
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** System Management Homepage
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-587/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise System Management Homepage. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of /proxy/SetSMHData requests. When parsing admin-group, operator-group, or user-group parameters, the process copies user-supplied data into a fixed-length stack buffer. A remote attacker can leverage this vulnerability to execute remote code under the context of the process.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-c05320149

## Disclosure Timeline

- 2016-05-09 - Vulnerability reported to vendor
- 2016-11-02 - Coordinated public release of advisory
