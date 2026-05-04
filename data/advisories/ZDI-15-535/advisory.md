# ZDI-15-535: Hewlett-Packard Vertica Remote Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-535
- **ZDI-CAN:** ZDI-CAN-2914
- **Date:** 2015-11-02
- **CVE:** CVE-2015-6867
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Vertica
- **Credit:** kjczi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-535/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Vertica. Authentication is not required to exploit this vulnerability. The specific flaw exists within the vertica-udx-zygote process, which listens on a random port in the ephemeral range. This process accepts an unauthenticated command packet to execute an arbitrary command under the context of dbadmin.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hpe.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04873095

## Disclosure Timeline

- 2015-05-06 - Vulnerability reported to vendor
- 2015-11-02 - Coordinated public release of advisory
